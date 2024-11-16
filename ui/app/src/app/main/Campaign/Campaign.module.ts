import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CAMPAIGN_MODULE_DECLARATIONS, CampaignRoutingModule} from  './Campaign-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CampaignRoutingModule
  ],
  declarations: CAMPAIGN_MODULE_DECLARATIONS,
  exports: CAMPAIGN_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CampaignModule { }