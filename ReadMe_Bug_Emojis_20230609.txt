# ReadMe_Bug_Emojis_20230609.txt
# C:\Users\email\OneDrive\DesktopSP7\JY_pyTools\Emojis\ReadMe_Bug_Emojis_20230609.txt
# Created 6/09/2023

[Heroku Error Message]
2023-06-09T17:39:11.572991+00:00 heroku[router]: at=error code=H20 desc="App boot timeout" method=GET path="/" host=raw-emojis.herokuapp.com request_id=c77ee494-154c-461a-85d2-9f9040ae621a fwd="69.244.23.198" dyno= connect= service= status=503 bytes= protocol=https

2023-06-09T17:39:20.357833+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch

2023-06-09T17:39:20.385378+00:00 heroku[web.1]: Stopping process with SIGKILL

2023-06-09T17:39:20.541084+00:00 heroku[web.1]: Process exited with status 137

2023-06-09T17:39:20.572301+00:00 heroku[web.1]: State changed from starting to crashed

2023-06-09T17:39:21.223923+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=raw-emojis.herokuapp.com request_id=ed8ce07e-8fc6-486e-a04b-5bca3f1ac2d9 fwd="69.244.23.198" dyno= connect= service= status=503 bytes= protocol=https

=> I think heroku does not support favicon.ico readily.
https://stackoverflow.com/questions/60987613/issues-deploying-to-heroku-path-path-favicon-ico
https://www.google.com/search?client=firefox-b-1-d&q=does+heroku+server+support+favicon.ico%3F
Maybe I should deploy this app to streamlit cloud instead.

############################### END OF DOCUMENT ##################################
