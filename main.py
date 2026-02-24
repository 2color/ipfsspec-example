import fsspec


def main():
    cid = "ipfs://bafybeicn7i3soqdgr7dwnrwytgq4zxy7a5jpkizrvhm5mv6bgjd32wm3q4/welcome-to-IPFS.jpg"

    with fsspec.open(cid, "rb", gateway="https://ipfs.io") as f:
        image_data = f.read()
        print(f"Retrieved {len(image_data)} bytes")

    with fsspec.open(
        "ipfs://bafkreie7ohywtosou76tasm7j63yigtzxe7d5zqus4zu3j6oltvgtibeom",
        "rb",
        gateway="https://ipfs.io",
    ) as f:
        image_data = f.read()
        print(f"Retrieved {len(image_data)} bytes")


if __name__ == "__main__":
    main()
