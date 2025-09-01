from nicegui import ui

ui.label("Hello Python Cohort!")
ui.button("Click Me")
ui.html("<h1 class='text-4xl'> this is a boy </h1>")
ui.image('https://picsum.photos/id/377/640/360')
v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
v.on('ended', lambda _: ui.notify('Video playback completed'))

ui.run()