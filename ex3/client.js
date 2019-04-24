var polo = require('polo');
var apps = polo();

apps.once('up', function(name, service) {
    console.log(apps.get(name));
});
