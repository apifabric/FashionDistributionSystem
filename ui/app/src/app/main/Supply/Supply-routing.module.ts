import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplyHomeComponent } from './home/Supply-home.component';
import { SupplyNewComponent } from './new/Supply-new.component';
import { SupplyDetailComponent } from './detail/Supply-detail.component';

const routes: Routes = [
  {path: '', component: SupplyHomeComponent},
  { path: 'new', component: SupplyNewComponent },
  { path: ':id', component: SupplyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Supply-detail-permissions'
      }
    }
  }
];

export const SUPPLY_MODULE_DECLARATIONS = [
    SupplyHomeComponent,
    SupplyNewComponent,
    SupplyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplyRoutingModule { }