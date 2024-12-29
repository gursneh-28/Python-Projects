import yt_dlp

def downloader():
        url = input("Enter url : ")
        try :
            yt = yt_dlp.YoutubeDL().extract_info(url, download=False)
        except yt_dlp.utils.DownloadError:
            print("Invalid URL !")
            return
        ydl_opt = {'format' : 'best', 'outtmpl' : '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opt) as ydl:
            print("Downloading...")
            ydl.download([url])
            print("Download Completed!")
       
        print("Metadata - ")
        print(f"Title : {yt.get('title', 'N/A')}")
        print(f"Uploader : {yt.get('uploader', 'N/A')}")
        print(f"Views : {yt.get('view_count', 'N/A')}")
        print(f"Duration : {yt.get('duration', 'N/A')} seconds")
        upload_date = yt.get('upload_date', 'N/A')
        if upload_date!='N/A' and len(upload_date) == 8:
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
            print(f"Upload date : {upload_date} ")

downloader()   