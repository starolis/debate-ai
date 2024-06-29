# AI Debate Simulator

This project simulates an engaging debate between two advanced AI models: GPT-4 and Claude. It provides an interactive platform where users can input debate topics and moderate a spirited discussion between these two AI participants.

## Features

- Interactive debate simulation between GPT-4 and Claude
- User-driven topic selection and moderation
- Dynamic conversation flow with alternating speaker order
- Witty and concise responses from AI participants

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- OpenAI API key
- Anthropic API key

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/starolis/debate-ai.git
   cd debate-ai
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your API keys:

   ```bash
   OPENAI_API_KEY='your_openai_api_key_here'
   ANTHROPIC_API_KEY='your_anthropic_api_key_here'
   ```

## Usage

To start a debate, run the following command:

```bash
python debate_ai.py
```

Follow the prompts to:

1. Enter a debate topic
2. Watch as GPT-4 and Claude exchange arguments
3. Provide new topics or questions as the moderator
4. End the debate when satisfied

## Sample Debate

```console
Enter the debate topic: Is artificial intelligence a threat to humanity?

Round 1
Moderator: Is artificial intelligence a threat to humanity?

GPT:
[GPT-4's response]

Claude:
[Claude's response]

Moderator (press Enter to continue, or type 'end' to finish): Should AI be regulated?

Round 2
Moderator: Should AI be regulated?

[Debate continues...]
```

## Customization

You can adjust the following parameters in the `debate_ai.py` file:

- `MAX_TOKENS`: Maximum number of tokens for AI responses
- AI models used (currently set to GPT-4o and Claude 3.5 Sonnet)
- System prompts for each AI to set the debate tone

## Contributing

Contributions to the AI Debate Simulator are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for the GPT-4o model
- Anthropic for the Claude 3.5 Sonnet model
- All contributors and users of this project

## Disclaimer

This project is for educational and entertainment purposes only. The AI models may produce biased or incorrect information. Always critically evaluate AI-generated content.
