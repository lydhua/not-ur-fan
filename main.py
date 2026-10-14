from instagram_client import get_instagram_data
from analyzer import analyze_followers

def main():
    try:
        followers, following = get_instagram_data()

        results = analyze_followers(followers, following)

        print(f"Followers: {len(followers)}")
        print(f"Following: {len(following)}")
        print(f"Not following back: {len(results)}\n")

        for index, username in enumerate(results, start=1):
            print(f"{index}. {username}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()