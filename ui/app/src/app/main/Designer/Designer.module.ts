import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DESIGNER_MODULE_DECLARATIONS, DesignerRoutingModule} from  './Designer-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DesignerRoutingModule
  ],
  declarations: DESIGNER_MODULE_DECLARATIONS,
  exports: DESIGNER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DesignerModule { }