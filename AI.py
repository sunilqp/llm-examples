{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO58k2m1I9ZW2cCUigMVNXi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sunilqp/llm-examples/blob/main/AI.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2vv2_u0TfI-T",
        "outputId": "9c81e52b-56e9-4c22-be37-8cceef3ec754"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting assemblyai\n",
            "  Downloading assemblyai-0.20.2-py3-none-any.whl (63 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m63.6/63.6 kB\u001b[0m \u001b[31m454.0 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting httpx>=0.19.0 (from assemblyai)\n",
            "  Downloading httpx-0.26.0-py3-none-any.whl (75 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.9/75.9 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pydantic!=1.10.7,>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from assemblyai) (1.10.13)\n",
            "Requirement already satisfied: typing-extensions>=3.7 in /usr/local/lib/python3.10/dist-packages (from assemblyai) (4.5.0)\n",
            "Collecting websockets>=11.0 (from assemblyai)\n",
            "  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.2/130.2 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.19.0->assemblyai) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.19.0->assemblyai) (2023.11.17)\n",
            "Collecting httpcore==1.* (from httpx>=0.19.0->assemblyai)\n",
            "  Downloading httpcore-1.0.2-py3-none-any.whl (76 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m76.9/76.9 kB\u001b[0m \u001b[31m7.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx>=0.19.0->assemblyai) (3.6)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.19.0->assemblyai) (1.3.0)\n",
            "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx>=0.19.0->assemblyai)\n",
            "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m4.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio->httpx>=0.19.0->assemblyai) (1.2.0)\n",
            "Installing collected packages: websockets, h11, httpcore, httpx, assemblyai\n",
            "Successfully installed assemblyai-0.20.2 h11-0.14.0 httpcore-1.0.2 httpx-0.26.0 websockets-12.0\n"
          ]
        }
      ],
      "source": [
        "pip install assemblyai"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# `pip3 install assemblyai` (macOS)\n",
        "# `pip install assemblyai` (Windows)\n",
        "\n",
        "import assemblyai as aai\n",
        "\n",
        "aai.settings.api_key = \"28af214d30bc482da80c11743451527c\"\n",
        "transcriber = aai.Transcriber()\n",
        "\n",
        "transcript = transcriber.transcribe(\"https://storage.googleapis.com/aai-web-samples/news.mp4\")\n",
        "# transcript = transcriber.transcribe(\"./my-local-audio-file.wav\")\n",
        "\n",
        "print(transcript.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DG_qShV9fuFm",
        "outputId": "f146c6d9-790f-45c3-8cbb-236e109bd5db"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "I'm David Curley at the Smithsonian Aaron Space Museum, where we are marking 50 years since man landed and walked on the moon in a lander just like this one. We are going to show you some of the actual ABC News coverage from 50 years ago during that eight day mission of this remarkable achievement, Apollo eleven's lander, the Eagle, would be the first manned craft to land on the moon. For training, NASA came with an unusual contraption. Neil Armstrong actually had to eject from it once, and then he had a couple of successful flights. ABC News anchor at the time, 50 years ago, Frank Reynolds with a look at that unusual trainer. Apollo eleven commander Neil Armstrong is at the controls of a lunar landing training vehicle, testing the reaction control jets. These thrusters stabilize the LEM during landing and takeoff. The LLTV is designed to simulate the behavior of the LEM as it lands in the moon's gravity. Lunar gravity is one 6th that of the Earth's. Neil Armstrong flew one of these vehicles on May 6, 1968, and that flight was nearly his last. Later reports by a NASA investigating team said the crash, which we'll see soon, was caused by a loss of fuel pressure compounded by a warning light that failed to work. Armstrong's coolness under pressure saved himself and possibly months of delay for the Apollo program. Later that same year, 1968, another test pilot, Joseph Allegrandi, also escaped from an LLTV just before it crashed. The training vehicle then underwent several design modifications and improvements. Engineers had to increase the vehicle's rocket power to help stabilize the craft. That made the LLTV less of a moon gravity simulator, but it improved pilot safety. On June 16, 1969, Neil Armstrong flew the vehicle, sometimes called the flying bedstead, to several perfect landings. Question was, how does the machine fly? And the answer is that we're very pleased with the way it flies. It's a significant improvement over the LLRV, which we were flying here a year ago, and I think it does an excellent job of actually capturing the handling characteristics of the lunar module in a landing maneuver. It's really a great deal different than any other kind of aircraft that I've ever flown. The, the simulation of lunar gravity has some aspects that make this type of flight sufficiently different from anything else we've ever done to make this vehicle very worthwhile. And I'm very pleased that I had the opportunity to get some flights in it here just before the Apollo eleven flight.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Start by making sure the `assemblyai` package is installed.\n",
        "# If not, you can install it by running the following command:\n",
        "# pip install -U assemblyai\n",
        "#\n",
        "# Note: Some macOS users may need to use `pip3` instead of `pip`.\n",
        "\n",
        "import assemblyai as aai\n",
        "\n",
        "# Replace with your API key\n",
        "aai.settings.api_key = \"28af214d30bc482da80c11743451527c\"\n",
        "\n",
        "# URL of the file to transcribe\n",
        "FILE_URL = \"https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3\"\n",
        "\n",
        "# You can also transcribe a local file by passing in a file path\n",
        "# FILE_URL = './path/to/file.mp3'\n",
        "\n",
        "config = aai.TranscriptionConfig(auto_highlights=True)\n",
        "\n",
        "transcriber = aai.Transcriber()\n",
        "transcript = transcriber.transcribe(\n",
        "  FILE_URL,\n",
        "  config=config\n",
        ")\n",
        "\n",
        "for result in transcript.auto_highlights.results:\n",
        "  print(f\"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "127fmr62gPFi",
        "outputId": "85b565c2-1ee7-4f75-e53e-83b901e2bc59"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Highlight: air quality alerts, Count: 1, Rank: 0.08\n",
            "Highlight: wide ranging air quality consequences, Count: 1, Rank: 0.08\n",
            "Highlight: more fires, Count: 1, Rank: 0.07\n",
            "Highlight: more wildfires, Count: 1, Rank: 0.07\n",
            "Highlight: air pollution, Count: 1, Rank: 0.07\n",
            "Highlight: weather systems, Count: 3, Rank: 0.07\n",
            "Highlight: high levels, Count: 2, Rank: 0.06\n",
            "Highlight: health conditions, Count: 1, Rank: 0.06\n",
            "Highlight: New York City, Count: 1, Rank: 0.06\n",
            "Highlight: respiratory conditions, Count: 1, Rank: 0.05\n",
            "Highlight: New York, Count: 3, Rank: 0.05\n",
            "Highlight: climate change, Count: 3, Rank: 0.05\n",
            "Highlight: air quality warnings, Count: 1, Rank: 0.05\n",
            "Highlight: Smoke, Count: 6, Rank: 0.05\n",
            "Highlight: heart conditions, Count: 1, Rank: 0.05\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#https://www.assemblyai.com/docs/speech-to-text/speech-recognition\n",
        "import assemblyai as aai\n",
        "\n",
        "aai.settings.api_key = \"28af214d30bc482da80c11743451527c\"\n",
        "\n",
        "audio_url = \"https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3\"\n",
        "\n",
        "transcriber = aai.Transcriber()\n",
        "\n",
        "transcript = transcriber.transcribe(audio_url)\n",
        "\n",
        "print(transcript.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJ25nqfyglGb",
        "outputId": "5b7afbaa-1e83-471e-c6ff-b5f00b123736"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Smoke from hundreds of wildfires in Canada is triggering air quality alerts throughout the US. Skylines from Maine to Maryland to Minnesota are gray and smoggy. And in some places, the air quality warnings include the warning to stay inside. We wanted to better understand what's happening here and why, so we called Peter DiCarlo, an associate professor in the department of Environmental Health and Engineering at Johns Hopkins University. Good morning. Professor good morning. So what is it about the conditions right now that have caused this round of wildfires to affect so many people so far away? Well, there's a couple of things. The season has been pretty dry already, and then the fact that we're getting hit in the US is because there's a couple of weather systems that are essentially channeling the smoke from those canadian wildfires through Pennsylvania into the mid Atlantic and the northeast and kind of just dropping the smoke there. So what is it in this haze that makes it harmful? And I'm assuming it is, is it is. The levels outside right now in Baltimore are considered unhealthy. And most of that is due to what's called particulate matter, which are tiny particles, microscopic, smaller than the width of your hair, that can get into your lungs and impact your respiratory system, your cardiovascular system, and even your neurological, your brain. What makes this particularly harmful? Is it the volume of particulate? Is it something in particular? What is it exactly? Can you just drill down on that a little bit more? Yeah. So the concentration of particulate matter I was looking at, some of the monitors that we have was reaching levels of what are, in science speak, 150 micrograms per meter cubed, which is more than ten times what the annual average should be and about four times higher than what you're supposed to have on a 24 hours average. And so the concentrations of these particles in the air are just much, much higher than we typically see. And exposure to those high levels can lead to a host of health problems. And who is most vulnerable? I noticed that in New York City, for example, they're canceling outdoor activities. And so here it is in the early days of summer, and they have to keep all the kids inside. So who tends to be vulnerable in a situation like this? It's the youngest. So children, obviously, whose bodies are still developing, the elderly who know their bodies are more in decline and they're more susceptible to the health impacts of breathing, the poor air quality. And then people who have preexisting health conditions, people with respiratory conditions or heart conditions, can be triggered by high levels of air pollution. Could this get worse? That's a good, in some areas it's much worse than others, and it just depends on kind of where the smoke is concentrated. I think New York has some of the higher concentrations right now, but that's going to change as that air moves away from the New York area. But over the course of the next few days, we will see different areas being hit at different times with the highest concentrations. I was going to ask you more fires start burning. I don't expect the concentrations to go up too much higher. I was going to ask you, and you started to answer this, but how much longer could this last? Or, forgive me if I'm asking you to speculate, but what do you think? Well, I think the fires are going to burn for a little bit longer, but the key for us in the US is the weather system changing. And so right now it's kind of the weather systems that are pulling that air into our mid Atlantic and northeast region. As those weather systems change and shift, we'll see that smoke going elsewhere and not impact us in this region as much. And so I think that's going to be the defining factor. And I think the next couple of days we're going to see a shift in that weather pattern and start to push the smoke away from where we are. And finally, with the impacts of climate change, we are seeing more wildfires. Will we be seeing more of these kinds of wide ranging air quality consequences or circumstances? I mean, that is one of the predictions for climate change. Looking into the future, the fire season is starting earlier and lasting longer, and we're seeing more frequent fires. So, yeah, this is probably something that we'll be seeing more frequently. This tends to be much more of an issue in the western US. So the eastern us getting hit right now is a little bit new. But, yeah, I think with climate change moving forward, this is something that is going to happen more frequently. That's Peter DiCarlo, associate professor in the department of Environmental Health and engineering at Johns Hopkins University. Thanks so much for joining us and sharing this expertise with us. Thank you for having me.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Set the words you want to search for\n",
        "words = [\"wildfires\", \"bar\", \"foo bar\", \"42\"]\n",
        "\n",
        "matches = transcript.word_search(words)\n",
        "\n",
        "for match in matches:\n",
        "    print(f\"Found '{match.text}' {match.count} times in the transcript\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3u2wBj9yhTZV",
        "outputId": "ed5c0bb0-be96-4389-b93b-c1cb1b6fa159"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 'wildfires' 4 times in the transcript\n"
          ]
        }
      ]
    }
  ]
}