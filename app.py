from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """
You are a professional customer support agent.
Write polite, clear, and helpful responses to customer issues.
Do not promise refunds or compensation unless certain.
Keep the tone friendly and professional.
"""

def generate_response(customer_message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=SYSTEM_PROMPT + "\nCustomer message: " + customer_message
        )

        return response.text if response.text else "No response generated"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("=== Customer Support AI (Gemini) ===")

    user_input = input("Enter customer message: ")

    output = generate_response(user_input)

    print("\n--- AI Response ---")
    print(output)

    with open("output.txt", "w") as f:
        f.write(output)

    print("\nSaved to output.txt")