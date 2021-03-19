from distutils.core import setup
setup(
  name = 'Readytousebot',         # How you named your package folder (MyLib)
  packages = ['Readytousebot'],   # Chose the same as "name"
  version = '1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Ready to use Discord.py bot',   # Give a short description about your library
  author = 'Rukchad Wongprayoon',                   # Type in your name
  author_email = 'mooping3roblox@gmail.com',      # Type in your E-Mail   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['discord.py', 'codeisboring', 'easy'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'discord-ext-alternatives',
          'discord',
          'aiofiles',
          'json',
          'asyncio',
          'functools',
          'itertools',
          'youtube_dl',
          'async_timeout'

      ],
  classifiers=[
    'Development Status :: 1 - Test',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.9.2',
  ],
)