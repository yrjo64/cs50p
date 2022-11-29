
def main():
    fn = input("File name: ").strip().lower()
    ext = fn.split(".").pop()
    match ext:
        case "gif":
            media_type = "image/gif"
        case "jpg" | "jpeg":
            media_type = "image/jpeg"
        case "png":
            media_type = "image/png"
        case "pdf":
            media_type = "application/pdf"
        case "txt":
            media_type = "text/plain"
        case "zip":
            media_type = "application/zip"
        case _:
            media_type ="application/octet-stream"
    print(media_type)
      
            
main()
            
        