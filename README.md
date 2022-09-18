# Raven by Affinity

C*a*n **yo**u ***re*ad** this? Most likely, your answer is yes. But with 15% of the global population being afflicted with reading disorders, and approximately 2.2 billion people worldwide with near or distance vision impairment, this answer is far from universal. Raven aims to fix this, by providing a product that increases accessibility to language and comprehension in a simple pair of spectacles.

## What it does

Raven uses the AdHawk vision tracking glasses to determine where in the world users are looking. It then uses optical character recognition (OCR) to read any text in a persons line of sight, and pipes it through a text-to-speech engine to read that text out loud for them. With Raven, people with vision impairments no longer need to despair over struggling to read, and those who benefit from an auditory cue while learning may have a tool to supplement their engagement with the written word.

## How we built it

Raven was built using the AdHawk Mindlink and their proprietary API that accompanies it. Their API allowed for focus, gaze, and eye tracking, which allows us to easily situate our user in their world, and identify the objects around them. This information is then piped through the Tesseract OCR algorithm, which returns a corpus of text that the user is trying to read. Finally, this text goes through the PyTTS text-to-speech engine, which translate the written word into the spoken one. 

## Challenges we ran into

One of our main challenges was the architecture of the AdHawk mind-link. Their backend software, required for establishing a connection between the headset and the computer, was Windows only. This meant we couldn't use it in a mobile setting, which would have been ideal for the project. It also limited the amount of testing and development we could do, as half our team had Macbooks. Another challenge we had was with optimization and efficiency: our current solution runs image processing on every frame fed from the headset. This means the software is not the most responsive for all forms of text and inputs. The amount of pre-processing applied is also minimal, which means viewing text at an angle is difficult, as there is no compensation for skew.

## Accomplishments that we're proud of

We are proud of successfully linking all three components together relatively seamlessly. Using the AdHawk MindLink was an amazing and educational experience for all of us, and taught us a lot about image processing, data cleaning, and how to write code that considers both efficiency and efficacy. We are also proud of how effective the OCR model is at reading text. 

## What we learned

All of us used AdHawk for the first time this hackathon. Many of us also learned about data cleaning, OCR, and TTS for the first time. For most of the members on our team, this was their first hackathon. We all learned that choosing a project idea wasn't as easy as it sounds, and that sometimes optimal solutions in theory still have limitations in practice. 

## What's next for Raven

Raven is set to grow as AdHawk's platform grows. Our future goals are setting up a remote backend that removes the need of a desktop OS for connecting the devices. Also, we intend to take advantage of multithreading to allow for the constant collection of image and text data while the TTS engine is running. Finally, we hope to write and optimize our own OCR engine such that we can control the efficiency and efficacy and hopefully find a medium that works best for our product. Our long term goal for this is a set of smart glasses that go far and beyond just optics in their pursuit of improving vision impairments.
