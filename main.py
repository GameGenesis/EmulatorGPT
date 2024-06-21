from openai import OpenAI
from config import model, temperature, prompt
import os

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def main():
    client = OpenAI()

    clear()
    print("EmulatorGPT\n")
    game = input("Enter the name of the game: ")
    clear()

    messages = [{"role": "system", "content": prompt.format(game=game)}]
    response = ""

    while True:
        stream = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="")
        
        messages.append({"role": "assistant", "content": response})
        
        choice = input("\nEnter your choice: ")
        print("\n")
        clear()
        messages.append({"role": "user", "content": choice})

if __name__ == "__main__":
    main()