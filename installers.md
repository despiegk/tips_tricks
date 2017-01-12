
```bash
#install jumpscale (CAREFUL, will remove /opt/*)
js 'c=j.tools.cuisine.get("ovh4");c.development.js8.install(reset=True)'

js 'c=j.tools.cuisine.get("ovh4");c.development.golang.install(reset=True)'

#get mongodb
js 'c=j.tools.cuisine.get("ovh4");c.apps.mongodb.install()'
#get ardb
js 'c=j.tools.cuisine.get("ovh4");c.apps.ardb.install()'

#get syncthing
js 'c=j.tools.cuisine.get("ovh4");c.apps.syncthing.install()'
```
