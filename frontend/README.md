# ⚛ cra-template
An opiniated template to set up a React project.

![GIF of project](xxx.png)

[▶ Live Preview](https://creme332.github.io/)

# 🚀Features
- HTML with appropriate SEO tags
- React Router v6
- Meyer CSS Reset
- CSS modules
- Useful packages such as `uniqid` 

#  🛠 Installation

Clone project:
```sh
git clone git@github.com:creme332/cra-template.git
```

## Placing project inside another project
⚠ If you are placing this project in another Git project `.git` folder, delete the `.git` folder in this project to prevent interference.

Update/delete the LICENSE file as well.
In `package.json`, update project name, description and homepage.

Install dependencies:
```sh
npm install
```

**IMPORTANT** : If your app is served from a sub-directory on your server, you’ll want to set `basename` in `RouteSwitch.js` to the sub-directory. A properly formatted basename should have a leading slash, but no trailing slash.

# Usage

### `npm run start`
Run project.

### `npm run build`
Generate production build.


### `npm run test`
Run Jest tests.

# To-do
- [ ] Write tests using Jest
- [ ] Create RouteSwitch file, add nav bar, fill home page file
- [ ] Generate production build
- [ ] Use pageInsight to test website after deployment.