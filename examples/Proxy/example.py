from abc import abstractmethod, ABCMeta


class ImageRepo(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str) -> str:
        pass


class RemoteImageRepo(ImageRepo):
    def get(self, key: str) -> str:
        return f"it's image for {key} \n"


class ImageCacheRepo(ImageRepo):
    def __init__(self, repo: RemoteImageRepo) -> None:
        self.cache = dict()
        self.remote = repo

    def get(self, key: str) -> str:
        if key not in self.cache:
            print("getting image from remote repository")
            self.cache[key] = self.remote.get(key)
        else:
            print("getting image from cache repository")

        return self.cache[key]


class ImageDownloader:
    def download_image(self, key, repo: ImageRepo):
        print(repo.get(key))


if __name__ == "__main__":
    downloader = ImageDownloader()
    remote_repo = RemoteImageRepo()
    cache_repo = ImageCacheRepo(remote_repo)

    downloader.download_image("cat_image_key", cache_repo)
    downloader.download_image("dog_image_key", cache_repo)
    downloader.download_image("cat_image_key", cache_repo)

    '''
    getting image from remote repository
    it's image for cat_image_key 

    getting image from remote repository
    it's image for dog_image_key 

    getting image from cache repository
    it's image for cat_image_key 
    
    '''
