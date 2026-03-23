from config.config_loader import Config

class AIProviderRouter:

    @staticmethod
    def generate(prompt: str):
        provider = Config.DEFAULT_AI_PROVIDER.lower()

        if provider == "openai":
            return AIProviderRouter._openai(prompt)
        elif provider == "anthropic":
            return AIProviderRouter._claude(prompt)
        elif provider == "gemini":
            return AIProviderRouter._gemini(prompt)
        else:
            return "Unsupported provider."

    @staticmethod
    def _openai(prompt):
        from openai import OpenAI
        client = OpenAI(api_key=Config.OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    @staticmethod
    def _claude(prompt):
        import anthropic
        client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)

        msg = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text

    @staticmethod
    def _gemini(prompt):
        import google.generativeai as genai
        genai.configure(api_key=Config.GEMINI_API_KEY)

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text
