!pip install google-generativeai
import google.generativeai as genai


genai.configure(api_key='your_API')

# Read the content of the clean text file
try:
    with open("clean_text.txt", "r", encoding="utf-8") as f:
        input_text = f.read()
except FileNotFoundError:
    print("Error: 'clean_text.txt' not found. Please run the preceding cells first.")
    input_text = ""

if input_text:

    model = genai.GenerativeModel('gemini-1.5-pro') 


    prompt = f"Summarize the following text:\n\n{input_text}"

    try:
        response = model.generate_content(prompt)
        output_text = response.text

        # Save the generated text to an output file
        with open("output_from_genai.txt", "w", encoding="utf-8") as f:
            f.write(output_text)

        print("Generated text saved to 'output_from_genai.txt'")
        print("\nGenerated Output:")
        print(output_text)

    except Exception as e:
        print(f"An error occurred during content generation: {e}")
else:
    print("No input text to process.")