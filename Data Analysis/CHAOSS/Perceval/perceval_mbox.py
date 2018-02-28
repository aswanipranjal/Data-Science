from perceval.backends.core.mbox import MBox

mbox_uri = 'http://mail-archives.apache.org/mod_mbox/httpd-announce/'
mbox_dir = 'archives'

repo = MBox(uri=mbox_uri, dirpath=mbox_dir)

for message in repo.fetch():
	print(message['data']['Subject'])