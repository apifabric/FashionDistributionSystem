import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CampaignHomeComponent } from './home/Campaign-home.component';
import { CampaignNewComponent } from './new/Campaign-new.component';
import { CampaignDetailComponent } from './detail/Campaign-detail.component';

const routes: Routes = [
  {path: '', component: CampaignHomeComponent},
  { path: 'new', component: CampaignNewComponent },
  { path: ':id', component: CampaignDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Campaign-detail-permissions'
      }
    }
  },{
    path: ':campaign_id/Participation', loadChildren: () => import('../Participation/Participation.module').then(m => m.ParticipationModule),
    data: {
        oPermission: {
            permissionId: 'Participation-detail-permissions'
        }
    }
}
];

export const CAMPAIGN_MODULE_DECLARATIONS = [
    CampaignHomeComponent,
    CampaignNewComponent,
    CampaignDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CampaignRoutingModule { }