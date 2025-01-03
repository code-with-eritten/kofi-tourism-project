from openai import OpenAI


def query(user_question, api_key):
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Kofi Tour giving information about torism in ghana.."},
                {"role": "user", "content": f"nUser question: {user_question}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


