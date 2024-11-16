import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DesignerHomeComponent } from './home/Designer-home.component';
import { DesignerNewComponent } from './new/Designer-new.component';
import { DesignerDetailComponent } from './detail/Designer-detail.component';

const routes: Routes = [
  {path: '', component: DesignerHomeComponent},
  { path: 'new', component: DesignerNewComponent },
  { path: ':id', component: DesignerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Designer-detail-permissions'
      }
    }
  },{
    path: ':designer_id/Collection', loadChildren: () => import('../Collection/Collection.module').then(m => m.CollectionModule),
    data: {
        oPermission: {
            permissionId: 'Collection-detail-permissions'
        }
    }
},{
    path: ':designer_id/Participation', loadChildren: () => import('../Participation/Participation.module').then(m => m.ParticipationModule),
    data: {
        oPermission: {
            permissionId: 'Participation-detail-permissions'
        }
    }
},{
    path: ':designer_id/Supply', loadChildren: () => import('../Supply/Supply.module').then(m => m.SupplyModule),
    data: {
        oPermission: {
            permissionId: 'Supply-detail-permissions'
        }
    }
}
];

export const DESIGNER_MODULE_DECLARATIONS = [
    DesignerHomeComponent,
    DesignerNewComponent,
    DesignerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DesignerRoutingModule { }