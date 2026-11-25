for f in *.opus; do
  ffmpeg -y -i "$f" -c:a pcm_s16le -ar 48000 "${f%.*}.wav"
done