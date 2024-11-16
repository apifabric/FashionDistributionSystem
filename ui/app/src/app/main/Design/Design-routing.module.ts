import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DesignHomeComponent } from './home/Design-home.component';
import { DesignNewComponent } from './new/Design-new.component';
import { DesignDetailComponent } from './detail/Design-detail.component';

const routes: Routes = [
  {path: '', component: DesignHomeComponent},
  { path: 'new', component: DesignNewComponent },
  { path: ':id', component: DesignDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Design-detail-permissions'
      }
    }
  },{
    path: ':design_id/Stock', loadChildren: () => import('../Stock/Stock.module').then(m => m.StockModule),
    data: {
        oPermission: {
            permissionId: 'Stock-detail-permissions'
        }
    }
}
];

export const DESIGN_MODULE_DECLARATIONS = [
    DesignHomeComponent,
    DesignNewComponent,
    DesignDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DesignRoutingModule { }