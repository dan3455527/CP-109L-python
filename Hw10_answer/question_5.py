import webbrowser

print("----Menu----")
print("Google\nPortal\nGithub\n")
choice = input("input the website to browse")

if choice == "google":
    webbrowser.open("https://www.google.com.tw/?client=safari")
elif choice == "portal":
    webbrowser.open("https://portalx.yzu.edu.tw/PortalSocialVB/Login.aspx")
elif choice == "github":
    webbrowser.open("https://github.com")
else:
    print("not an option")