import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CollectionHomeComponent } from './home/Collection-home.component';
import { CollectionNewComponent } from './new/Collection-new.component';
import { CollectionDetailComponent } from './detail/Collection-detail.component';

const routes: Routes = [
  {path: '', component: CollectionHomeComponent},
  { path: 'new', component: CollectionNewComponent },
  { path: ':id', component: CollectionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Collection-detail-permissions'
      }
    }
  },{
    path: ':collection_id/Design', loadChildren: () => import('../Design/Design.module').then(m => m.DesignModule),
    data: {
        oPermission: {
            permissionId: 'Design-detail-permissions'
        }
    }
}
];

export const COLLECTION_MODULE_DECLARATIONS = [
    CollectionHomeComponent,
    CollectionNewComponent,
    CollectionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CollectionRoutingModule { }