import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedModule } from '../../shared/shared.module';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
      path: 'test1',
      loadChildren: () => import('./test1/test1.module').then(m => m.Test1Module)
  }
]

@NgModule({
  declarations: [],
  imports: [SharedModule, RouterModule.forChild(routes)],
  providers: []
})
export class TstModModule { }
