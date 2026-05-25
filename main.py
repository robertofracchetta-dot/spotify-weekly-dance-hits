import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os

print("🚀 Weekly Dance Hits by Roberto Fracchetta DJ")
print("   Aggiornamento Automatico da Agenti AI\n")

# ================== CONFIGURAZIONE ==================
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
PLAYLIST_ID = "5sbONO1I7Ky6G0NZviCDAz"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public playlist-modify-private"
))

def clear_playlist():
    print("🧹 Svuoto completamente la playlist...")
    results = sp.playlist_tracks(PLAYLIST_ID, limit=100)
    tracks = [item['track']['uri'] for item in results['items'] if item.get('track')]
    
    if tracks:
        for i in range(0, len(tracks), 4):
            batch = tracks[i:i+4]
            try:
                sp.playlist_remove_all_occurrences_of_items(PLAYLIST_ID, batch)
                print(f"   Rimossi {len(batch)} brani...")
                time.sleep(7)
            except:
                time.sleep(8)
        print("✅ Playlist svuotata completamente")
    else:
        print("✅ Playlist già vuota")

clear_playlist()

print("\n✅ Playlist pronta per ricevere le 30 tracce selezionate dagli Agenti AI questa settimana.")
print("   (La selezione verrà fatta ogni Lunedì)")
