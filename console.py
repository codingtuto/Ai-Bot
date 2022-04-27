# Copyright New-dev0 & Coding Team 2022

print(
    """

░█████╗░██╗░░██╗░█████╗░████████╗██████╗░░█████╗░████████╗
██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
██║░░╚═╝███████║███████║░░░██║░░░██████╦╝██║░░██║░░░██║░░░
██║░░██╗██╔══██║██╔══██║░░░██║░░░██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝██║░░██║██║░░██║░░░██║░░░██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░
\n\n"""
)

try:
    import requests
except ImportError:
    print("'requests' module non installé.")
    print("Installer le script et exécuter sur le console.")
    exit()

print("Enter 'pour quitter entrer n'importe quoi..")

CV_HNDLR = {}

print("Entrer votre message.")


def main(inpt):
    if inpt == "'exit":
        exit()
    json = {"userMessageText": inpt}
    if CV_HNDLR:
        json.update({"conversationId": CV_HNDLR["_"]})
    _ = requests.post("https://services.bingapis.com/sydney/chat", json=json).json()
    if not _.get("messages") and "has expired." in _["result"]["message"]:
        del CV_HNDLR["_"]
        main(inpt)
        return
    for msg in _["messages"]:
        if msg["author"] == "bot":
            print(">>", msg["text"])
            if msg.get("hiddenText"):
                print("\n\n>>", msg["hiddenText"])
            if msg.get("sourceName"):
                print(">>\n-", msg["sourceName"], "\n-", msg["sourceUrl"])
            if msg.get("linkUrl"):
                print(">> -", msg["linkUrl"])
    if not CV_HNDLR:
        CV_HNDLR["_"] = _["conversationId"]


while True:
    inpt = input("> ")
    main(inpt)
