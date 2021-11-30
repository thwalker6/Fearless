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