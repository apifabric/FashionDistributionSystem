import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PARTICIPATION_MODULE_DECLARATIONS, ParticipationRoutingModule} from  './Participation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ParticipationRoutingModule
  ],
  declarations: PARTICIPATION_MODULE_DECLARATIONS,
  exports: PARTICIPATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ParticipationModule { }