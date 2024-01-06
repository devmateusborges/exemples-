import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { SharedModule } from './../shared/shared.module';
import { AppLoginComponent } from './app-login/app-login.component';


const routes: Routes = [
  { path: 'login', component: AppLoginComponent },

];


@NgModule({
  declarations: [AppLoginComponent],
  imports: [
    SharedModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forChild(routes),
  ]
})
export class AuthModule { }
