import random
import asyncio


async def generate_ai_response(user_input: str):

    await asyncio.sleep(0.5)


    if not user_input:
        raise Exception(
            "Invalid input: User input is empty"
        )


    # Simulated AI failures
    failure_chance = random.random()


    if failure_chance < 0.15:
        raise Exception(
            "AI model timeout: Response generation failed"
        )


    if "unclear" in user_input.lower():
        raise Exception(
            "AI confusion: Unable to understand input"
        )


    response = {
        "message": "AI response generated successfully",
        "analysis": (
            f"I analyzed your request: {user_input}"
        ),
        "confidence": round(
            random.uniform(0.80, 0.99),
            2
        )
    }


    return response
