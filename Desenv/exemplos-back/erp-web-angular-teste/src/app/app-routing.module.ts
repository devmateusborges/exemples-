import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppNotAuthComponent } from './shared/components/app-not-auth/app-not-auth.component';
import { AppNotFoundComponent } from './shared/components/app-not-found/app-not-found.component';
import { AppMenuInitComponent } from './shared/components/app-menu-init/app-menu-init.component';


const routes: Routes = [
  { path: '', redirectTo: 'menu-init', pathMatch: 'full' },
  { path: 'menu-init', component: AppMenuInitComponent },
  { path: 'tst-mod', loadChildren: () => import('./pages/tst-mod/tst-mod.module').then(m => m.TstModModule) },
  //
  { path: 'app-app-not-auth', component: AppNotAuthComponent },
  { path: 'app-app-not-found', component: AppNotFoundComponent },
  { path: '**', redirectTo: 'app-app-not-found' }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
