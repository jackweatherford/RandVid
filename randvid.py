from moviepy.editor import *
from numpy import arange
from random import shuffle

filename = input('Enter filename: ')

print('\nExtracting frames...')

clip = VideoFileClip(filename)

time_per_frame = 1 / clip.fps

num_frames = round(clip.duration * clip.fps)

new_clip = []
i = 0
while len(new_clip) < num_frames:
	new_clip.append(clip.subclip(i, i + time_per_frame))
	
	i += time_per_frame
	
	print(f'{len(new_clip)/num_frames*100:.2f}%', end="\r")

print('\nDone!\n\nShuffling frames...')

shuffle(new_clip)

new_clip = concatenate_videoclips(new_clip)
split_filename = filename.split('.')
print('100.00%\nDone!\n\nWriting to file...')
new_clip.write_videofile(f'{".".join(split_filename[:-1])}_randomized.mp4', fps=clip.fps)

print('\nDone!')
