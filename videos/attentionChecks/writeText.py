from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os

i=0
file = "es_attention_select22.mp4"
if file.endswith(".mp4"):
    video = VideoFileClip(file)

    # if ("13" in file) or ("23" in file):
    #     i=4
    # elif ("12" in file) or ("22" in file):
    #     i=3
    # elif ("11" in file) or ("21" in file):
    #     i=2
    # elif ("10" in file) or ("20" in file):
    #     i=1

    text = TextClip(
    #   text=f"Esta es una prueba\n de atención.\n Por favor, pon este\n vídeo en la \nposición {i} \n empezando por la\nizquierda.",
        font="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        # text=f"Esta es una prueba\n de atención.\n\n Por favor, \nselecciona\neste vídeo.",
        # text=f"Hau atentzio proba\n bat da.\n\n Mesedez,\n Aukeratu bideo\nhau.",
        # text=f"Hau atentzio proba\n bat da.\n\n Mesedez,\n ez aukeratu bideo\nhau.",
        text=f"Esta es una prueba\n de atención.\n\n Por favor,\nno selecciones\n este vídeo.",
        font_size=70,
        color="white",
        text_align="center",
        duration=video.duration - 5,
    )
    # Start displaying the text at 5 seconds
    text = text.with_start(5).with_position(("center", "center"))

    output = CompositeVideoClip([video, text])
    newName = file.replace(".mp4", "_text.mp4")

    output.write_videofile(newName)