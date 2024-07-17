import requests

def summarize_text(text):
    api_url = "http://localhost:11434/api"  # Replace with actual API endpoint
    headers = {
        "Authorization": "cat ~/.ollama/id_ed25519.pub",
        # Replace with your API key
        "Content-Type": "application/json"  
    }
    payload = {
        "model": "Qwen2-0.5B",
        "text": text
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        summary = response.json().get("summary", "No summary found.")
    else:
        summary = f"Error: {response.status_code} - {response.text}"
    
    return summary

if __name__ == '__main__':
    text = "The quick brown fox jumped over the lazy dog."
    summary = summarize_text(text)
    print("Summary:", summary)
