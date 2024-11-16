import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ParticipationHomeComponent } from './home/Participation-home.component';
import { ParticipationNewComponent } from './new/Participation-new.component';
import { ParticipationDetailComponent } from './detail/Participation-detail.component';

const routes: Routes = [
  {path: '', component: ParticipationHomeComponent},
  { path: 'new', component: ParticipationNewComponent },
  { path: ':id', component: ParticipationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Participation-detail-permissions'
      }
    }
  }
];

export const PARTICIPATION_MODULE_DECLARATIONS = [
    ParticipationHomeComponent,
    ParticipationNewComponent,
    ParticipationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ParticipationRoutingModule { }