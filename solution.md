So this is the first initial git request to set it up in the repo.  Honestly I feel like Ill have a little fun with this part since its the first pull request for this little project.  There will be some time stamps far apart, Ill be walking away here and there to play with my son, do my job, or decorate my house for Christmas.  Anyways here is a basic run down of how I will set up the application.

Using FastAPI establish a basic api for an Item.  Make it so you can add/remove/get items in either bulk or as a single one.
0) Set up a readme and a git repo 
1) Set up a model for the item (ID, Name).  To add an item only an ID and name must be provided.  An item cannot be added with the same ID but they can have the same name as another item.  Initial set up will be done in memory.
2)To call an item they can either searh by ID or by name.  If multiple items have the same name both objects will be returned.
3) Deleting an item can only be done by ID since multiple items can share a name.  
4) Set up a mongo db in docker to store the data. Then update the process to pull from the mongo db instead of memory.
5) Deploy the api to docker.
6) Test the api.
7) complain that it doesnt work
8) get it to work because I missed something small
9) Obsessivley go over my work before submitting
10) Finally submit my work.


Would adds:
Additional unit test.  It has good coverage not great.  I figured the amount added was enough to show whats going on.
Additional properties to items.  Currently there are only 2 properties, name and ID.  I put it in a mongodb since it would make it easier to add stuff.
Would seperate db stuff from the service into a seperate component.  Makes it simpler in some regards.
different environmental configurations/ports
Security/Access.  I mean its an api, you need some protection on it.  This has none.

Things I did for the first time here:
Patched a mongodb through for a connection.  I have practically only dealt with SQL databases so noSQL is a bit new to me. Patching in a mongodb was a bit new to me, and very little documentaiton on how to do it in this type of scenario.  I kind of winged it.
Setting up mongodb in a docker file with the environment to have everything run at once.  Had to watch some "fun" youtube videos on that.
