from fastapi import FastAPI
from pydantic import BaseModel
from random import random
from fastapi.middleware.cors import CORSMiddleware
import resend
import config as cfg

resend.api_key = cfg.EMAIL_API_KEY

class Participant(BaseModel):
  name: str
  email: str

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=['*'],
  allow_headers=['*'],
)

def send_email(pairing):
  print(f"{pairing[0].email}: Hello {pairing[0].name}. Drawing is completed. Give something special to {pairing[1].name}")
  
  if not cfg.EMAIL_DEBUG_MODE:
    email = resend.Emails.send({
      "from": cfg.EMAIL_SENDER_ADDRESS,
      "to": [cfg.EMAIL_DEBUG_ADDRESS],
      "subject": f"Hello {pairing[0].name}. Drawing is completed",
      "html": f"Give something special to {pairing[1].name}",
    })
    print(email)
  else:
    print("Debug mode. Email is not sent.")

@app.get("/")
def hello_world_endpoint():
  return { "Hello": "World" }


@app.post("/draw_pairings/")
def draw_pairings(participants: list[Participant]):
  shuffledParticipants = sorted(participants, key = lambda x: random() - 0.5)
  pairings = []
  for i in range(len(shuffledParticipants)):
    pairing = (shuffledParticipants[i], shuffledParticipants[(i + 1) % len(shuffledParticipants)])
    pairings.append(pairing)
    send_email(pairing)

