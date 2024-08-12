import requests

def upload_video_to_facebook(video_url, access_token, page_id):
    payload = {
        'access_token': access_token,
        'title': 'Your Video Title',
        'description': 'Your Video Description',
        'file_url': video_url
    }

    response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos', data=payload)
    return response.json()

if __name__ == "__main__":
    video_url = 'https://drive.google.com/uc?export=download&id=15uucSWkSdHOFEn9YjmwpRDh4PZOegvD8'
    access_token = 'EAAOAouTfDpsBO7xc2qazzBJQoZBorXfHE8j7ZAJEhmmtT0ChmXSmx7yj7wgVeXzsvkFZBVi9b8UBvXAmgXw9rICiZB1zWusPCbw4KVmClrTB7bOzKlyyN6fHxnrnvRkTw8A70RGTUN0M0nC5UL511ci4TmFBkIb0eAEtqmwZArwKYRcsjwnCgKvaTwaPmBPYZD'
    page_id = '247607515094289'
    print(upload_video_to_facebook(video_url, access_token, page_id))
