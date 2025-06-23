

from dotenv import load_dotenv # type: ignore
import os
from agents import Agent, Runner, AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig # type: ignore

load_dotenv()
gemini_api_key= os.getenv("OPENROUTER_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     

agent = Agent(
    name = "Writer Agent",
    instructions = " you are awriter agent. Generate Stories,Poems,Essay etc "
)
response = Runner.run_sync(
    agent,
    input= "write a short essay on Quaid-e-Azam in simple English ",
    run_config = config
)

print(response)

