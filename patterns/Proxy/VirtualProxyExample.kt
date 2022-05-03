// 가상(virtual) 프록시 예제: 지연 초기화
interface ImageViewer {
    fun showImage()
}

class RealImageViewer(path: String) : ImageViewer {
    // 객체 생성 시점에 이미지 로딩이라는 무거운 작업을 미리 수행
    private val image: Image = Image.load(path)

    override fun showImage() {
        image.show()
    }
}

class ProxyImageViewer(private val path: String) : ImageViewer {
    // 실제 이미지 뷰어 객체를 미리 만들지 않고, 생성에 필요한 path 정보만 들고 있음
    private lateinit var imageViewer: ImageViewer

    override fun showImage() {
        if (!::imageViewer.isInitialized) {
            // 필요한 시점에 초기화
            imageViewer = RealImageViewer(path)
        }
        imageViewer.showImage()
    }
}
