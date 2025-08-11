import os
from dotenv import load_dotenv

# elevenlabs modules
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# monkey-patch: add user_id to ConversationConfig dynamically
if "user_id" not in ConversationConfig.__annotations__:
    ConversationConfig.__annotations__["user_id"] = str
    setattr(ConversationConfig, "user_id", None)

# load API credentials
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

if not AGENT_ID or not API_KEY:
    raise EnvironmentError("Missing AGENT_ID or API_KEY in .env")

# varaibles
user_name = "Jcodes"
schedule = "Apple Code session today at 2pm EST"
prompt = f"You are a helpful assistant. You have the following schedule: {schedule}"
first_message = f"Hello {user_name}, how can I assist you today?"

# configuration to ElevenLabs agent ======================
dynamic_vars = {
    "user_name": user_name,
}

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig (
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables=dynamic_vars,
)
# assign user_id at creation time
object.__setattr__(config, "user_id", "Jcodes")

# ElevenLabs client is given the key to start working
client = ElevenLabs(api_key=API_KEY)
# ========================================================

# callback functions for responses
'''
this is used to handle assistant reponses by printing the assistant's
and the user transcripts, and also handles the situation where the
agent may be interrupted.
'''
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# start voice assistant session
#   this is used to initiate the session
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()
