import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { FormsModule } from '@angular/forms';
//
import {ButtonModule} from 'primeng/button';
import {DividerModule} from 'primeng/divider';
import {CheckboxModule} from 'primeng/checkbox';
import {InputTextModule} from 'primeng/inputtext';
//
import { AppMenuInitComponent } from './components/app-menu-init/app-menu-init.component';
import { AppMenuTopComponent } from './components/app-menu-top/app-menu-top.component';
import { AppNotAuthComponent } from './components/app-not-auth/app-not-auth.component';
import { AppNotFoundComponent } from './components/app-not-found/app-not-found.component';
import { AppMenuSideComponent } from './components/app-menu-side/app-menu-side.component';

@NgModule({
  imports: [
  ],
  declarations: [AppMenuTopComponent, AppNotAuthComponent, AppNotFoundComponent,AppMenuInitComponent, AppMenuSideComponent],
  exports: [
    CommonModule,
    TranslateModule,
    FormsModule,
    //
    ButtonModule,
    DividerModule,
    CheckboxModule,
    InputTextModule]
})
export class SharedModule { }
