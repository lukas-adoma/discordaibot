#from discord.ext import voice_recv
from elevenlabs.client import ElevenLabs
import os

'''

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    # Connect using the VoiceRecvClient for receive capability
    voice_client = await channel.connect(cls=voice_recv.VoiceRecvClient)
    # Save voice_client for later use (see below)

'''

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
intro_text = "Hello ! I am your voice assistant."  
audio_data = elevenlabs_client.text_to_speech.convert(
    text=intro_text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",   # default voice ID (example)
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128"
)
# Save audio to file
with open("intro.mp3", "wb") as f:
    for chunk in audio_data:
        f.write(chunk)
# Play the intro in the voice channel
#voice_client.play(discord.FFmpegPCMAudio("intro.mp3"))