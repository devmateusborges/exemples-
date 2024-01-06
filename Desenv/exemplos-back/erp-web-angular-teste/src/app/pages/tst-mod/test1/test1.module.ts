import { SharedModule } from './../../../shared/shared.module';
import { NgModule } from '@angular/core';
import { Test1Component } from './test1.component';
import { RouterModule, Routes } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';


const routes: Routes = [
  { path: '', component: Test1Component },
  { path: 'new', component: Test1Component },
  { path: ':id/edit', component: Test1Component }
];

@NgModule({
  imports: [SharedModule, RouterModule.forChild(routes), ReactiveFormsModule, ],
  declarations: [Test1Component],
})
export class Test1Module { }


