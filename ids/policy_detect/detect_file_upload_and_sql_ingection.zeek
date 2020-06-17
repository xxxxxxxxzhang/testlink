##! Test RememberMe deserialization attack detection.

@load base/protocols/http/main.zeek
@load base/protocols/http/utils.zeek
@load base/frameworks/notice
@load base/frameworks/sumstats
@load base/protocols/http

module HTTP;

export {
    ## Describes the type of notice we will generate with the Notice framework.
    ## Notices allow Zeek to generate some kind of extra notification beyond its default log types.
    redef enum Notice::Type += {
        File_Upload_Attack,
        Sql_Ingection_Attack
    };
    
}

redef FileExtract::prefix = "./";

global test_file_analysis_source: string = "" &redef;

global test_file_analyzers: set[Files::Tag];

global test_get_file_name: function(f: fa_file): string =
	function(f: fa_file): string { return ""; } &redef;

global test_print_file_data_events: bool = F &redef;

global file_count: count = 0;

global file_map: table[string] of count;


event file_state_remove(f: fa_file)
	{
  local file_content:string ="";
  
	if ("POST" in f$http$method )
          {
          if("sqlmap" in f$http$user_agent)
              {
                print(f$http$user_agent);
                print(f$http$uri);
                local m: Notice::Info = Notice::Info($note=Sql_Ingection_Attack, 
                                                 $msg="Sql_Ingection", 
                                                 $sub=f$http$user_agent,
                                                 $f=f
                                                 );
               NOTICE(m);
                
              }
          }
  if (f?$bof_buffer )
		{
     
      if ("POST" in f$http$method &&  "upload" in f$bof_buffer)
          {
          local a: Notice::Info = Notice::Info($note=File_Upload_Attack, 
                                                 $msg="file upload", 
                                                 $sub=f$http$uri,
                                                 $f=f
                                                 );
          NOTICE(a);
          }
      if ( "logs" in f$http$uri )
          {
            file_content=f$bof_buffer;
            print(file_content);
            local n: Notice::Info = Notice::Info($note=File_Upload_Attack, 
                                                 $msg="get shell", 
                                                 $sub=file_content,
                                                 $f=f
                                                 );
            NOTICE(n);
          }
      
		}
  
	}

