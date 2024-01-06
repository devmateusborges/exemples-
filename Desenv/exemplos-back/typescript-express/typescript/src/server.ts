import App from '@/app';
import AuthRoute from '@routes/auth.route';
import IndexRoute from '@routes/index.route';
import SysUsersRoute from '@routes/sysUser.route';
import validateEnv from '@utils/validateEnv';

validateEnv();

const app = new App([new IndexRoute(), new SysUsersRoute(), new AuthRoute()]);

app.listen();
